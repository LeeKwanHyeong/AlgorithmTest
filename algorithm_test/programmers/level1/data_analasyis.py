# PCCE 기출문제 10번 / 데이터분석

def solution(data, ext, val_ext, sort_by):
    # filtering and sorting index mapping
    index_map = {
        'code' : 0,
        'date' : 1,
        'maximum' : 2,
        'remain' : 3,
    }
    
    # filter index setting
    filter_index = index_map.get(ext, 0)
    
    # filtering
    filtered_data = [item for item in data if item[filter_index] < val_ext]
    
    # sorting and set index
    sort_index = index_map.get(sort_by, 0)
    filtered_data.sort(key=lambda x: x[sort_index])
    
    
    return filtered_data