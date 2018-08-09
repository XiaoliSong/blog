import os
from blog.config import POST_PREFIX_PAHT
from single_post import generate_single_post
from post_json import generate_post_json
from recommend import generate_recommend
from tag import generate_tag
from page import generate_pages

def generate_all_posts():
    cnt=0
    for dir_name in os.listdir(POST_PREFIX_PAHT):
        path_dir_name=os.path.join(POST_PREFIX_PAHT,dir_name)
        if(os.path.isdir(path_dir_name)):
            generate_single_post(dir_name)
            cnt+=1
    print("生成全部帖子成功，共："+str(cnt)+"个")
    generate_post_json()
    generate_pages()
    generate_recommend()
    generate_tag()

if __name__=="__main__":
    generate_all_posts()