// 搜索初始化
(function(){
	function get_query_string(name) {
		let reg = new RegExp("(^|&|\\?)" + name + "=([^&]*)(&|$)", "i");
		let r = window.location.search.substr(1).match(reg);
		if (r != null) return decodeURIComponent(r[2]); 
		return null;
	}

    let key_word=get_query_string('key_word');
    if (key_word != null){
        document.getElementById('search_input').value = key_word;

        let cmp_similarity = function(key, str){
            key = key.toLowerCase()
            str = str.toLowerCase()
            
            key_map = new Map()
            for(let i in key) {
                if (key[i] in key_map){
                    key_map[key[i]]++
                }
                else{
                    key_map[key[i]] = 1
                }
            }

            str_map = new Map()
            for(let i in str) {
                if (str[i] in str_map){
                    str_map[str[i]]++
                }
                else{
                    str_map[str[i]] = 1
                }
            }
            
            cnt = 0;
            sum = 0;
            for (c in key_map){
                value = key_map[c]
                if (str_map.hasOwnProperty(c)){
                    cnt = cnt + Math.min(value, str_map[c])
                }
                sum = sum + value;
            };
            return cnt / sum;
        }

        let show_result = function(data){
            post_json = JSON.parse(data)
            res_post_arr = []
            for (let post_link in post_json){
                post = post_json[post_link]
                similarity = cmp_similarity(key_word, post['title'])
                if (post.hasOwnProperty("tags")){
                    for(i in post['tags']){
                        c1 = cmp_similarity(post['tags'][i], key_word)
                        c2 = cmp_similarity(key_word, post['tags'][i])
                        similarity = Math.max(similarity,c1,c2)
                    }
                }

                if (similarity > 0){
                    if (post.hasOwnProperty("tags")){
                        res_post_arr.push({
                            "link": post_link,
                            "title": post['title'],
                            "tags": post['tags'],
                            "similarity": similarity
                        })
                    }
                    else{
                        res_post_arr.push({
                            "link": post_link,
                            "title": post['title'],
                            "similarity": similarity
                        })
                    }
                }
            }
            res_post_arr.sort(function(x,y){
                return y['similarity'] - x['similarity']
            })

            document.getElementById('search_result').innerHTML = "<p class = 'search_noti'>搜索匹配结果" + res_post_arr.length + "条</p>";
            ul = document.createElement("ul");
            for(i in res_post_arr){
                post = res_post_arr[i];
                li = document.createElement("li");
                if (post.hasOwnProperty("tags")){
                    li.innerHTML = "<a title='标签：["+ post['tags'].toString()+"]' href='" + post['link'] + "'>" + post['title'] + '</a>'
                }
                else{
                    li.innerHTML = "<a href='" + post['link'] + "'>" + post['title'] + '</a>'
                }
                ul.appendChild(li)
            }
            document.getElementById('search_result').appendChild(ul)
        }

        const SessionKey = "search.json";
        data = sessionStorage.getItem(SessionKey);
        if (data == null){
            let json_url = "/search.json"
            let xhr = new XMLHttpRequest();            
            xhr.open('GET', json_url, true);
            xhr.onreadystatechange = function() {
                if (xhr.readyState == 4 && xhr.status == 200 || xhr.status == 304) {
                    data = xhr.responseText;
                    show_result(data);
                    sessionStorage.setItem(SessionKey, data);
                }
            };
            xhr.send();
        }
        else{
            show_result(data);
        }
    }
})();
