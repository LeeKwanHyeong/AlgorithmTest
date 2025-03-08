import java.io.*

/*
    백준 21921: [블로그]
    N: 블로그 시작한 일수
    X일 동안 가장 많이 들어온 방문자 수와 그 기간을 알기

*/
fun main() = with(File("21912_input.txt").bufferedReader()){
    val(N, X) = readLine().split(" ").map{ it.toInt() }
    val visitList = readLine().split(" ").map { it.toInt() }

    // 초기 윈도우 (처음 X일의 방문자 수 합)
    var currentSum = visitList.take(X).sum()
    var max = currentSum
    var count = 1

    // 슬라이딩 윈도우 적용
    for (i in X until N){
        // 새로운 방문자 추가, 가장 오래된 방문자 제거
        currentSum += visitList[i] - visitList[i - X] 

        when {
            currentSum > max -> {
                max = currentSum
                count = 1
            }
            currentSum == max -> count++
        }
    }


    // for ( i in visitList.indices){
    //     // 윈도우가 리스트 사이즈를 넘었을때는 멈춤
    //     if(i + X > visitList.size ) break

    //     var sum = 0
    //     for (j in i..i+X-1){
    //         sum += visitList[j]
    //         if(max < sum){
    //             max = sum
    //         } else if (max == sum) count++            
    //     }
    // }

    if(max==0) {println("SAD")}
    else {
        println(max)
        println(count)
    }
}