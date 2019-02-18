import sys
from blog.post import generate_all_posts_file
from blog.post import generate_changed_posts_file
from blog.post import generate_post_file

if __name__ == "__main__":
    if len(sys.argv) == 2:
        if sys.argv[1] == '-all':
            # 全部重新生成
            generate_all_posts_file()
        else:
            # 生成指定某个
            generate_post_file(sys.argv[1])
    else:
        # 只生成变化的
        generate_changed_posts_file()