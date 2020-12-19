package main

import (
	"bytes"
	"crypto/md5"
	"encoding/base64"
	"encoding/json"
	"fmt"
	"io/ioutil"
	"log"
	"net/http"
	"net/url"
	"sort"
	"strconv"
	"strings"
	"sync"
)

var httpSrv = NewHTTPMiddleware()

type HTTPMiddleware struct {
	cache sync.Map
}

func NewHTTPMiddleware() *HTTPMiddleware {
	obj := &HTTPMiddleware{}
	buf, err := ioutil.ReadFile("cache.tmp")
	if err != nil {
		return obj
	}
	m := make(map[string][]byte)
	err = json.Unmarshal(buf, &m)
	if err != nil {
		log.Println(err)
	}
	for key, val := range m {
		obj.cache.Store(key, val)
	}
	return obj
}

func (o *HTTPMiddleware) Get(url string) ([]byte, error) {
	hash := md5.New()
	hash.Write([]byte(url))
	h := hash.Sum(nil)
	key := base64.StdEncoding.EncodeToString(h)
	if val, ok := o.cache.Load(key); ok {
		return val.([]byte), nil
	}
	log.Printf("HTTP: url: %s \n", url)
	res, err := http.Get(url)
	if err != nil {
		return nil, err
	}
	buf, err := ioutil.ReadAll(res.Body)
	if err != nil {
		return nil, err
	}
	o.cache.Store(key, buf)
	return buf, nil
}

func (o *HTTPMiddleware) Post(url string, payload []byte) ([]byte, error) {
	hash := md5.New()
	hash.Write([]byte(url))
	hash.Write(payload)
	h := hash.Sum(nil)
	key := base64.StdEncoding.EncodeToString(h)
	if val, ok := o.cache.Load(key); ok {
		return val.([]byte), nil
	}
	log.Printf("HTTP: url: %s \n", url)
	res, err := http.Post(url, "application/json", bytes.NewBuffer(payload))
	if err != nil {
		return nil, err
	}
	buf, err := ioutil.ReadAll(res.Body)
	if err != nil {
		return nil, err
	}
	o.cache.Store(key, buf)
	return buf, nil
}

func (o *HTTPMiddleware) Flush() {
	// if _, err := os.Stat("cache.tmp"); err == nil {
	// 	return
	// }
	m := make(map[string][]byte)
	o.cache.Range(func(key, value interface{}) bool {
		m[key.(string)] = value.([]byte)
		return true
	})
	buf, err := json.Marshal(m)
	if err != nil {
		log.Println(err)
		return
	}
	err = ioutil.WriteFile("cache.tmp", buf, 0777)
	if err != nil {
		log.Println(err)
	}
}

type Request interface {
	DoRequest() error
}

type Difficulty struct {
	Level int `json:"level"`
}

type Stat struct {
	QuestionID        int    `json:"question_id"`
	TotalSubmitted    int    `json:"total_submitted"`
	TotalAcs          int    `json:"total_acs"`
	QuestionTitle     string `json:"question__title"`
	QuestionTitleSlug string `json:"question__title_slug"`
}

type Problem struct {
	Difficulty Difficulty `json:"difficulty"`
	Stat       Stat       `json:"stat"`
	Status     string     `json:"status"`
}

type ListProblemsAPI struct {
	StatStatusPairs []Problem `json:"stat_status_pairs"`
}

func (o *ListProblemsAPI) DoRequest() error {
	url := "https://leetcode.com/api/problems/all/"
	buf, err := httpSrv.Get(url)
	if err != nil {
		return err
	}
	return json.Unmarshal(buf, o)
}

type DiscussQuestionTopicTag struct {
	ID        string `json:"id"`
	Name      string `json:"name"`
	NumTopics int    `json:"numTopics"`
}

type DiscussQuestionTopicTags struct {
	DiscussQuestionTopicTags []DiscussQuestionTopicTag `json:"discussQuestionTopicTags"`
}

type DiscussQuestionTopicTagAPI struct {
	QuestionID string
	Data       DiscussQuestionTopicTags `json:"data"`
}

func (o *DiscussQuestionTopicTagAPI) DoRequest() error {
	url := "https://leetcode.com/graphql"

	payload := map[string]interface{}{
		"operationName": "discussQuestionTopicTags",
		"variables": map[string]interface{}{
			"questionId": o.QuestionID,
		},
		"query": "query discussQuestionTopicTags($tagType: String, $questionId: String!, $selectedTags: [String!]) {  discussQuestionTopicTags(tagType: $tagType, questionId: $questionId, selectedTags: $selectedTags) {    ...TopicTag    __typename  }}fragment TopicTag on DiscussTopicTagNode {  id  name  slug  numTopics  __typename}",
	}
	buf, err := json.Marshal(payload)
	if err != nil {
		return err
	}

	buf, err = httpSrv.Post(url, buf)
	if err != nil {
		return err
	}
	return json.Unmarshal(buf, o)
}

type QuestionTopicsListNodePost struct {
	VoteCount int    `json:"voteCount"`
	Status    string `json:"status"`
}

type QuestionTopicsListNodeTag struct {
	Name string `json:"name"`
}

type QuestionTopicsListNode struct {
	Id           string                      `json:"id"`
	Title        string                      `json:"title"`
	ViewCount    int                         `json:"viewCount"`
	CommentCount int                         `json:"commentCount"`
	Post         QuestionTopicsListNodePost  `json:"post"`
	Tags         []QuestionTopicsListNodeTag `json:"tags"`
}

type QuestionTopicsListEdge struct {
	Node QuestionTopicsListNode `json:"node"`
}

type QuestionTopicsList struct {
	Edges []QuestionTopicsListEdge `json:"edges"`
}

type QuestionTopicsListData struct {
	QuestionTopicsList QuestionTopicsList `json:"questionTopicsList"`
}

type QuestionTopicsListAPI struct {
	QuestionID string
	Data       QuestionTopicsListData `json:"data"`
}

func (o *QuestionTopicsListAPI) DoRequest() error {
	url := "https://leetcode.com/graphql"

	payload := map[string]interface{}{
		"operationName": "questionTopicsList",
		"variables": map[string]interface{}{
			"questionId": o.QuestionID,
			"first":      15,
			"orderBy":    "most_votes",
			"query":      "",
			"skip":       0,
			"tags":       []interface{}{},
		},
		"query": "query questionTopicsList($questionId: String!, $orderBy: TopicSortingOption, $skip: Int, $query: String, $first: Int!, $tags: [String!]) {\n  questionTopicsList(questionId: $questionId, orderBy: $orderBy, skip: $skip, query: $query, first: $first, tags: $tags) {\n    ...TopicsList\n    __typename\n  }\n}\n\nfragment TopicsList on TopicConnection {\n  totalNum\n  edges {\n    node {\n      id\n      title\n      commentCount\n      viewCount\n      pinned\n      tags {\n        name\n        slug\n        __typename\n      }\n      post {\n        id\n        voteCount\n        creationDate\n        isHidden\n        author {\n          username\n          isActive\n          profile {\n            userSlug\n            userAvatar\n            __typename\n          }\n          __typename\n        }\n        status\n        coinRewards {\n          ...CoinReward\n          __typename\n        }\n        __typename\n      }\n      lastComment {\n        id\n        post {\n          id\n          author {\n            isActive\n            username\n            profile {\n              userSlug\n              __typename\n            }\n            __typename\n          }\n          peek\n          creationDate\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    cursor\n    __typename\n  }\n  __typename\n}\n\nfragment CoinReward on ScoreNode {\n  id\n  score\n  description\n  date\n  __typename\n}\n",
	}
	buf, err := json.Marshal(payload)
	if err != nil {
		return err
	}

	buf, err = httpSrv.Post(url, buf)
	if err != nil {
		return err
	}
	return json.Unmarshal(buf, o)
}

type Question struct {
	QuestionID string `json:"questionId"`
	Content    string `json:"content"`
	Dislikes   int    `json:"dislikes"`
	Likes      int    `json:"likes"`
}

type QuestionDataData struct {
	Question Question `json:"question"`
}

type QuestionDataAPI struct {
	TitleSlug string
	Data      QuestionDataData `json:"data"`
}

func (o *QuestionDataAPI) DoRequest() error {
	url := "https://leetcode.com/graphql"

	payload := map[string]interface{}{
		"operationName": "questionData",
		"query":         "query questionData($titleSlug: String!) {  question(titleSlug: $titleSlug) {    questionId    questionFrontendId    boundTopicId    title    titleSlug    content    translatedTitle    translatedContent    isPaidOnly    difficulty    likes    dislikes    isLiked    similarQuestions    contributors {      username      profileUrl      avatarUrl      __typename    }    topicTags {      name      slug      translatedName      __typename    }    companyTagStats    codeSnippets {      lang      langSlug      code      __typename    }    stats    hints    solution {      id      canSeeDetail      paidOnly      hasVideoSolution      __typename    }    status    sampleTestCase    metaData    judgerAvailable    judgeType    mysqlSchemas    enableRunCode    enableTestMode    enableDebugger    envInfo    libraryUrl    adminUrl    __typename  }}",
		"variables": map[string]interface{}{
			"titleSlug": o.TitleSlug,
		},
	}

	buf, err := json.Marshal(payload)
	if err != nil {
		return err
	}

	buf, err = httpSrv.Post(url, buf)
	if err != nil {
		return err
	}
	return json.Unmarshal(buf, o)
}

type LeetCodeDiscussion struct {
	Id      string
	Title   string
	Content string
	Vote    int
	View    int
	Tag     []string
}

type LeetCodeBrief struct {
	Title      string
	Slug       string
	Difficulty int
	Like       int
	Unlike     int
	Discussion []LeetCodeDiscussion
}

type ByDifficulty []LeetCodeBrief

func (o ByDifficulty) Len() int { return len(o) }
func (o ByDifficulty) Less(i, j int) bool {
	if o[i].Difficulty == o[j].Difficulty {
		return o[i].Like > o[j].Like
	}
	return o[i].Difficulty < o[j].Difficulty
}
func (o ByDifficulty) Swap(i, j int) { o[i], o[j] = o[j], o[i] }

func (o LeetCodeBrief) Print() {
	link := fmt.Sprintf("https://leetcode.com/problems/%s", o.Slug)
	fmt.Printf("## [%s](%s) difficulty: %s, like: %d, dislike: %d \t\n", o.Title, link, difficultyName[o.Difficulty], o.Like, o.Unlike)
	for _, dis := range o.Discussion {
		tagStr := strings.Join(dis.Tag, ", ")
		discussionLink := fmt.Sprintf("%s/discuss/%s/%s", link, dis.Id, url.PathEscape(dis.Title))
		fmt.Printf("- [%s](%s) vote: %d view: %d tags: [%s] \n", dis.Title, discussionLink, dis.Vote, dis.View, tagStr)
	}
}

func main() {
	defer httpSrv.Flush()

	api := ListProblemsAPI{}
	err := api.DoRequest()
	if err != nil {
		log.Println(err)
	}

	var wg sync.WaitGroup

	leetcodeBriefs := make([]LeetCodeBrief, len(api.StatStatusPairs))
	for i, statPair := range api.StatStatusPairs {
		wg.Add(1)
		go func(i int, statPair Problem) {
			defer wg.Done()
			leetcodeBriefs[i], err = ShowQuestionDiscussion(statPair)
			if err != nil {
				log.Println(err)
			}
			// ShowTagsByKeyword(statPair, "merge")
		}(i, statPair)
	}
	wg.Wait()

	leetcodeBriefs = Filter(leetcodeBriefs, FilterByDifficulty("medium"))

	sort.Sort(ByDifficulty(leetcodeBriefs))
	for _, brief := range leetcodeBriefs {
		brief.Print()
	}
}

type FilterBy func(brief LeetCodeBrief) bool

func FilterByDifficulty(difficulty string) FilterBy {
	return func(brief LeetCodeBrief) bool {
		if strings.EqualFold(difficultyName[brief.Difficulty], difficulty) {
			return true
		}
		return false
	}
}

func Filter(briefs []LeetCodeBrief, filters ...FilterBy) []LeetCodeBrief {
	var leetcodeBriefs []LeetCodeBrief
	for _, brief := range briefs {
		isInclude := true
		for _, filter := range filters {
			if filter(brief) == false {
				isInclude = false
				break
			}
		}
		if isInclude {
			leetcodeBriefs = append(leetcodeBriefs, brief)
		}
	}
	return leetcodeBriefs
}

var difficultyName = map[int]string{
	1: "easy",
	2: "medium",
	3: "hard",
}

func ShowQuestionDiscussion(statPair Problem) (LeetCodeBrief, error) {
	questionAPI := QuestionDataAPI{TitleSlug: statPair.Stat.QuestionTitleSlug}
	err := questionAPI.DoRequest()
	if err != nil {
		return LeetCodeBrief{}, err
	}

	questionTopicsAPI := QuestionTopicsListAPI{QuestionID: strconv.Itoa(statPair.Stat.QuestionID)}
	err = questionTopicsAPI.DoRequest()
	if err != nil {
		return LeetCodeBrief{}, err
	}

	edges := questionTopicsAPI.Data.QuestionTopicsList.Edges
	if len(edges) > 5 {
		edges = edges[:5]
	}

	brief := LeetCodeBrief{
		Title:      statPair.Stat.QuestionTitle,
		Slug:       statPair.Stat.QuestionTitleSlug,
		Difficulty: statPair.Difficulty.Level,
		Like:       questionAPI.Data.Question.Likes,
		Unlike:     questionAPI.Data.Question.Dislikes,
		Discussion: nil,
	}

	for _, questionTopic := range edges {
		node := questionTopic.Node
		var tagSs []string
		for _, tag := range node.Tags {
			tagSs = append(tagSs, tag.Name)
		}
		brief.Discussion = append(brief.Discussion, LeetCodeDiscussion{
			Id:    node.Id,
			Title: node.Title,
			Vote:  node.Post.VoteCount,
			View:  node.ViewCount,
			Tag:   tagSs,
		})
	}
	return brief, nil
}

func ShowTagsByKeyword(statPair Problem, keyword string) {
	discussionAPI := DiscussQuestionTopicTagAPI{QuestionID: strconv.Itoa(statPair.Stat.QuestionID)}
	err := discussionAPI.DoRequest()
	if err != nil {
		log.Println(err)
		return
	}
	isContainTag := false
	var qualifiedTags []DiscussQuestionTopicTag
	for _, tag := range discussionAPI.Data.DiscussQuestionTopicTags {
		if len(keyword) != 0 && Contains(tag.Name, keyword) {
			isContainTag = true
			qualifiedTags = append(qualifiedTags, tag)
		}
	}
	if isContainTag {
		fmt.Printf("Problem: %s, solve: %s \n", statPair.Stat.QuestionTitle, statPair.Status)
		for _, tag := range qualifiedTags {
			fmt.Printf("\t Tag: %s \n", tag.Name)
		}
	}
}

func Contains(s string, subs string) bool {
	listS := strings.Split(subs, " ")
	for _, sub := range listS {
		if !strings.Contains(s, sub) {
			return false
		}
	}
	return true
}
