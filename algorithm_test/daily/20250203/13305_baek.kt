import java.io.*
/*
    [주유소]
    제일 왼쪽 도시에서 제일 오른쪽 도시로 자동차를 이용하여 이동하려 함 (도로의 길이 단위는 km)

    1. 처음 출발 시 기름 넣고 출발해야함 (기름통 크기는 무제한)
    2. 1km 당 1L 기름 사용
    3. 각 도시에는 단 하나의 주유소, 도시 마다 주유소의 리터당 가격은 다름 (가격 단위: 원)
*/
fun main() = with(File("13305_input.txt").bufferedReader()){
    val N = readLine().toInt()
    val distances = readLine().split(" ").map{ it.toLong() }
    val prices = readLine().split(" ").map { it.toLong() }

    var minPrice = prices[0] // 초기 최소 기름값은 첫 번째 도시의 가격
    // var totalCost = 0L //총 비용

    // for (i in 0 until N-1){
    //     // 현재 최소 가격으로 주유
    //     println("totalCost = $totalCost, minPrice = $minPrice distances[i], ${distances[i]}")
    //     totalCost += minPrice * distances[i]
    //     println("Added totalCost = $totalCost")

    //     // 더 싼 기름이 나오면 갱신
    //     if (prices[i + 1] < minPrice){
    //         minPrice = prices[i + 1]
    //         println("minPrice = $minPrice")
    //     }
    // }
    val totalCost = distances.foldIndexed(0L){ i, acc, distance -> 
        val cost = minPrice * distance
        if(i + 1 < prices.size && prices[i + 1] < minPrice) {
            minPrice = prices[i+1]
        }
        acc + cost
    }

    println(totalCost)

}