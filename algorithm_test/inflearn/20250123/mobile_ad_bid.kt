import java.io.*
// import java.io.BufferReader
// import java.io.File
// import java.io.FileReader

fun main() {
    // readln(), readLine()
    val path = "input.txt"
    val reader = BufferedReader(FileReader(File(path)))

    // N: 광고 지면 수, K: 목표 낙찰 지면 수
    var (N, K) = reader.readLine().split(" ").map { it.toInt() }
    var count = 0
    println("N: $N, K: $K")

    // Ai : MOLOCO가 제시한 입찰 가격 
    // Bi: MOLOCO를 제외한 다른 모든 입찰 가 중 최고 가격
    // MOLOCO의 입찰가에서 Ai를 이괄적으로 X만큼 올렸을때
    // K개 이상의 지면을 낙찰받게 되는 가장 작은 음이아닌 정수 X를 찾자
    
    // val arr = MutableList<List<Int>>(N) {
    //     (reader.readLine().split(" ").map { it.toInt() }).toList()
    // }

    val arr = Array(N) { reader.readLine().split(" ").map { it.toInt() }.toList() }

    println(arr.contentToString())
    while(N != 0){
        arr.forEach { item -> 
            if(item[0] > item[1]){
                N--
                // arr에서 해당 아이템을 pop하고
                println(arr.contentToString())
            }
        }

    }

}