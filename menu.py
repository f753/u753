from database import Database
from models.blog import Blog

__author__ = 'f753'

class Menu(object):
    def __init__(self):
        self.user = input("请输入你的用户名:")
        self.user_blog = None
        if self._user_has_account():
            print("Welcome back{}".format(self.user))
        else:
            self._prompt_user_for_account()
    def _user_has_account(self):
        blog = Database.find_one('blogs',{'author':self.user})
        if blog is not None:
            self.user_blog = blog
            return True
        else:
            return False

    def _prompt_user_for_account(self):
        title = input("请输入blog title:")
        description = input("请输入内容:")
        blog = Blog(author=self.user,
                    title=title,
                    description=description)
        blog.save_to_mongo()
        self.user_blog = blog
    def run_menu(self):
        read_or_write = input("你选择读（R）还是写(W)?")
        if read_or_write == "R":
            self._list_blogs()
            self._view_blog()
        elif read_or_write =="W":
            self.user_blog.new_post()
        else:
            print("谢谢你 请重新选")

    def _list_blogs(self):
        blogs = Database.find(collection='blogs',
                              query={})
        for blog in blogs:
            print("ID:{},Title:{},Author:{}".format(blog['id'],blog['title'],blog['author'],))

    def _view_blog(self):
        blog_to_see = input("请输入id：")
        blog = Blog.from_mongo(blog_to_see)
        posts = blog.get_posts()
        for post in posts:
            print("date:{},title:{}\n\n{}".format(post['created_date'],post['title'],post['content']))