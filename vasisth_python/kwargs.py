def func1(**kwargs):
    print(kwargs)

def func2(**kwargs):
    for k,v in kwargs.items():
        print(f"{k}:{v}")

func1(first_name='shubham',last_name='kumar')
func2(first_name='shubham',last_name='kumar')
d=dict(first_name='shubham',last_name='kumar')
func1(**d)