def solution(wallpaper):
    # 빈칸 "." , 파일 칸 "#"
    # 목적: 최소한의 이동거리를 갖는 한 번의 드래그, 모든 파일을 선택해서 한 번에 지우기
    # 마우스 클릭 S(lux, luy) -> 드래그 엔드포인트 E(rdx, rdy)
    # 거리 = abs(rdx-lux) + abs(rdy-luy)
    
    file_list = []
    
    wallpaper_list = [list(i) for i in wallpaper]
    
    for row_index, row_item in enumerate(wallpaper_list):
        for column_index, column_item in enumerate(wallpaper_list[row_index]):
            if wallpaper_list[row_index][column_index] == '#':
                file_list.append((row_index, column_index))
            
    
    sorted_list_row = sorted(file_list, key=lambda x: (x[0], x[1]))
    sorted_list_col = sorted(file_list, key=lambda x: (x[1], x[0]))
    

    start_point = [sorted_list_row[0][0], sorted_list_col[0][1]]
    end_point = [sorted_list_row[-1][0] + 1, sorted_list_col[-1][1] + 1]
    
    print(start_point)
    print(end_point)
    
    
    answer = [start_point[0], start_point[1], end_point[0], end_point[1]]
    
    return answer