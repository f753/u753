from database import Database
from models.blog import Blog
from models.post import Post
from menu import Menu

__author__ = 'f753'

Database.initialize()


menu = Menu()
menu.run_menu()


#
# post = Post(blog_id=2,
#             title="浮三网络科技2",
#             content="佛山市佛山网络科技有限公司2",
#             author="浮三2")
#
# post.save_to_mongo()


# post1 = Post("2","浮三网络科技有限公司2", "一家网络开发公司2", "浮三2")
#
# print(post.content)
# print(post1.content)

# 查询
# post = Post.from_mongo('c13b681ddd0a436dac207a4594bf1623')
# print(post)

# posts = Post.from_blog(2)
# print(posts)
# for post in posts:
#     print(post)

# blog = Blog(author="华",
#             title="浮三科技",
#             description="佛山市浮三科技")
#
# blog.new_post()
# blog.save_to_mongo()
# from_database = Blog.from_mongo(blog.id)
# print(blog.get_posts())

