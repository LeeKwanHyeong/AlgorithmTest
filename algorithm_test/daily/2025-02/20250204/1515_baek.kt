import java.io.*

/*
    백준 1515: [수 이어 쓰기]
    1부터 N까지 모든 수를 차례대로 공백없이 한 줄에 작성
    그 중 다솜이가 세준이가 쓴 수에서 마음에 드는 몇 개의 숫자 지움

    세준이가 다시 와서 전과 같이 똑같이 쓰려했지만 N이 기억나지 않는다.file
    
    남은 수를 이어 붙인 수가 주어질 때, N의 최솟값을 구하는 프로그램을 작성
    * 아무것도 지우지 않을 수도 있다.
*/

fun main() = with(File("1515_input.txt").bufferedReader()){
    val target = readLine() // 남은 숫자 문자열
    var index = 0 // target의 현재 탐색 위치
    var N = 0 // 결과로 출력한 최소의 N

    while(index < target.length){
        N++
        val current = N.toString() // 현재 숫자를 문자열로 반환

        // 현재 숫자의 각 자릿수를 target과 비교
        for (ch in current){
            if (index < target.length && ch == target[index]){
                index++
            }
        }
    }
    println(N)
}