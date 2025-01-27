20250127
1. Kotlin 에서 시간 초과를 넘기지 않기 위한 기본
   - item.split(" ")를 반복적으로 호출
     - ex)
     - mode = readline().split(" ").first()
     - x = readline().split(" ").last().toInt()
     - solution)
     - val parts = readline().split(" ")
     - mode = parts[0]
     - x = if(parts.size > 1) parts[1].toInt() else 0
  - 배열의 반복적 초기화
     - booleanArray().fill(true)
     - booleanArray().fill(false)
  - 출력결과 일괄 출력
     - StringBuilder() 사용


