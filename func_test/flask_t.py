from flask import Flask

app = Flask(__name__)


# 添加路由的几种方式
# 1.装饰器
@app.route("/hello")
def hello():
    return 'hello.'


# 2.调用add_url_rule()方法
def hello_chinese():
    return "hello."


app.add_url_rule('/hello_chinese', 'hello_chinese', hello_chinese)


# 3.直接操作url_map()
def hello_world():
    return 'Hello World!'


options = {}
endpoint = hello_world.__name__
options['endpoint'] = endpoint
methods = {'GET', 'OPTIONS'}
rule = app.url_rule_class("/", methods=methods, **options)
provide_automatic_options = getattr(hello_world, __name__, None)
rule.provide_automatic_options = endpoint
app.url_map.add(rule)
app.view_functions[endpoint] = hello_world

if __name__ == '__main__':
    print(app.url_map)
    app.run()
