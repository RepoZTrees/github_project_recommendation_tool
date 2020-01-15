import github_project

def test_fav_language():

    assert github_project.get_fav_language('repoZTrees') == 'Python'
    
def test_recommend_project():
    actual_value = ['Python','Ruby','Java','Python','Javscript']
    expected_value = 'Python'
    assert actual_value == expected_value
    
