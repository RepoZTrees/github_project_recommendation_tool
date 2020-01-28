import github_project

def test_fav_language():

    assert github_project.get_fav_language('repoZTrees') == 'Python'
    

def test_query_params():
    
    assert github_project.query_params() == {'q':'language:python', 'sort':'updated','order':'desc'}  
    assert github_project.query_params('ruby') == {'q':'language:ruby', 'sort':'updated','order':'desc'}

    
