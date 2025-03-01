import java.io.*

/*
    굴다리 모든 길 0 ~ N 을 밝히게 가로등 설치 요청
    인천광역시: 가로등 설치할 개수 M개, 가로등 위치 x 결정 완료
    -> 예산이 부족해져서, 최소한의 높이로 굴다리 모든 길 0~N을 밝히고자 한다.

    ** 최소한의 예산이 들 높이**
    condition1) 가로등은 모두 높이가 같아야 하고 정수.
    condition2) 가로등의 높이가 H라면 왼쪽으로 H, 오른쪽으로 H만큼 주위를 비춘다.

    N: 굴다리 길이
    M: 가로등 개수
    x: M개의 설치할 수 있는 가로등의 위치 (0 <= x <= N)

*/

fun main() = with(File("17266_input.txt").bufferedReader()){
    val N = readLine().toInt()             // 굴다리 길이
    val M = readLine().toInt()             // 가로등 개수
    val positions = readLine().split(" ").map { it.toInt() } // 가로등 위치 리스트

    var left = 0
    var right = N
    var result = N

    // 가로등 높이로 굴다리 전체를 비출 수 있는지 확인하는 함수
    fun canLightAll(H: Int): Boolean {
        var prev = 0
        // 첫 번째 가로등이 시작부터 커버 가능한지 확인
        if (positions[0] - H > 0) return false

        for (pos in positions) {
            println("H: $H prev: $prev pos: $pos")
            if (prev < pos - H) return false  // 어두운 구간 발생 시 불가능
            prev = pos + H                    // 다음 가로등이 비출 수 있는 마지막 위치
        }

        return prev >= N                     // 굴다리 끝까지 커버했는지 확인
    }

    // 이진 탐색 수행
    while (left <= right) {
        val mid = (left + right) / 2

        if (canLightAll(mid)) {
            result = mid          // 현재 높이로 커버 가능하면 최소 높이 갱신
            right = mid - 1       // 더 작은 높이 시도
        } else {
            left = mid + 1        // 더 큰 높이 필요
        }
    }

    println(result)               // 최소 높이 출력

}