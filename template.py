from jinja2 import Environment, FileSystemLoader #, FunctionLoader

class Template:
    def __init__(self):
        self.env = Environment(loader=FileSystemLoader('./', encoding='utf8'))
        self.name = "jinja2_test.tmpl"#いったんベタがき

    def render(self):
        tmpl = self.env.get_template(self.name)
        with open('jinja2_test.html',mode='w') as f:
            f.write(str(tmpl))
        #本当はreturnしたhtmlを描画したい
        #return tmpl.render(message=u"hello world from jinja2")

    # '''
    # ファイル名の検索
    # '''
    # def search(self):
    #     pass

if __name__ == "__main__":
    template = Template()
    template.render()