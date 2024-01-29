name = "test_function"   #глобальная переменная

def test_function():
    #name = "Другой"  #локальная переменная
    def inner_function():
        print("Я в области видимости " + name)
    inner_function()


test_function()

