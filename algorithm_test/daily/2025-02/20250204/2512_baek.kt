import java.io.*

/*
    백준 2512: [예산]
    정해진 총액 이하에서 가능한 한 최대의 총 예산을 다음과 같은 방법으로 배정한다.
    1. 모든 요청이 배정될 수 있는 경우에는 요청한 금액을 그대로 배정한다.
    2. 모든 요청이 배정될 수 없는 경우
     - 특정한 정수 상한액을 계산하여 그 이상인 예산요청에는 모두 상한액을 배정
     - 상한액 이하의 예산요청에 대해서는 요청한 금액 그대로 배정
*/
fun main() = with(File("2512_input.txt").bufferedReader()){
    val N = readLine().toInt()
    val requestList = readLine().split(" ").map { it.toInt() }.sortedBy { it }
    val maximum = readLine().toInt()

    var low = 0
    var high = requestList.maxOrNull()!!
    var result = 0

    while(low <= high){
        val mid = (low + high) / 2
        var total = 0L // 누적 합산 (오버플로 방지하기 위해 Long 사용)

        // 누적합으로 메모리 절약
        for(request in requestList){
            total += if(request > mid) mid else request
        }

        // 예산 초과 시 상한선 낮추기
        if (total > maximum){
            high = mid - 1
        } else {
            result = mid // 현재 상한선 저장
            low = mid + 1
        }
    }
    println(result)
}
// 4, 8, 12, 16, 20, 24, 28, 32, 36, 40
// 4, 8, 2, 6, 0, 