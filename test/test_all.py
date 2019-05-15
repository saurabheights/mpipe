def test_tiny(capsys):
    
    from mpipe import OrderedStage, Pipeline
    
    def increment(value):
        return value + 1

    def double(value):
        return value * 2

    stage1 = OrderedStage(increment, 3)
    stage2 = OrderedStage(double, 3)
    pipe = Pipeline(stage1.link(stage2))
    
    for number in range(10):
        pipe.put(number)
        
    pipe.put(None)

    for result in pipe.results():
        print(result)

    import os
    with open(os.path.join(os.path.dirname(__file__), 'tiny.gold')) as f:
        assert f.read() == capsys.readouterr().out
