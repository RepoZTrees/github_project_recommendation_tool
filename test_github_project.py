import github_project

def test_fav_language():

    #assert github_project.get_fav_language(['python','python','python','ruby','java','c','javascript']) == 'Python'
    assert github_project.get_fav_language('repoZTrees') == 'Python'
    
