import java.io.*

/*
    턴을 번갈아가며 돌을 1개 또는 3개로 가져갈 수 있다.
*/
fun main() = with(File("input.txt").bufferedReader()){
    val N = readLine().toInt()

    if (N % 2 == 0){
        println("CY")
    } else {
        println("SK")
    }
}