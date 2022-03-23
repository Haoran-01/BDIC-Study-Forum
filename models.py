# from db import db
#
# # 定义orm模型
# class User(db.Model):
#     __tablename__ = 'user_TEST'
#     user_id = db.Column(db.Integer, primary_key = True, autoincrement = True)
#     user_name = db.Column(db.String(200), nullable = False)
#     user_password = db.Column(db.Text, nullable = False)
#
# @app.route('/User')
# def user_view():
#     # 1.添加数据
#     user=User(title="zhangsan",content="XXX")
#     db.session.add(user)
#     ##做一个提交操作
#     db.session.commit()
#
#     #2.查询数据
#     #filter_by:返回一个类列表的对象
#     user=User.query.filter_by(id=1)[0]
#     print(user.title)
#
#     #3.修改数据
#     user=User.query.filter_by(id=1)[0]
#     user.content="yyy"
#     db.session.commit()
#
#     #4.删除数据
#     User.query.filter_by(id=1)[0].delete()
#     user.delete()
#     db.session.commit()
#
#     return "数据库操作成功"
