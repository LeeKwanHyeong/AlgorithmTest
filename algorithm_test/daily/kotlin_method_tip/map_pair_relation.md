# 📚 Kotlin에서 `Map<String, Int>`와 `Pair<String, Int>`의 관계 설명

---

## ✅ 1️⃣ 기본 개념

- **`Map<String, Int>`**는 **키-값 쌍(Key-Value Pair)**의 집합입니다.
- Kotlin에서는 `Map`의 각 요소가 내부적으로 **`Pair<Key, Value>` 형태**로 저장됩니다.

### 📌 예제
```kotlin
val dictMap = mapOf("apple" to 3, "banana" to 5)
println(dictMap.toList())
// output:: [(apple, 3), (banana, 5)]
```

- `toList()` 메서드는 `Map`을 `List<Pair<String, Int>>`로 변환한다.
- 즉, `Map`의 각 요소가 `(key, value)`쌍으로 리스트에 저장된다.

## ✅ 2️⃣ `sortedWith(compareByDescending<Pair<String, Int>>)`의 작동 원리
```kotlin
dictMap.toList()
    .sortedWith(compareByDescending<Pair<String, Int>> { it.second })
```
- `toList()`:
  - `Map`을 `List<Pair<String, Int>>`로 변환한다.
  - `Pair<String, Int>`의 구조는 `(key, value)` 이다.
- `compareByDescending<Pair<String, Int>>`:
  - `Pair`의 두 번째 요소인 `value`를 기준으로 내림차순 정렬한다.

## ✅ 3️⃣ 왜 `Pair<String, Int>`를 사용해야 할까?
### 문제: 왜 단순히 `compareByDescending { it.value } 를 사용하지 않을까?
- `Map`에는 `key`와 `value`라는 개념이 있지만, `toList()`로 변환하면 각 요소는 `Pair`가 되어 `first`와 `second`로 관리된다.
- 따라서, `it.second`를 사용하여 값에 접근해야 한다.

## ✅ 4️⃣ 실제 코드 분석
```kotlin
dictMap.toList()
    .sortedWith(compareByDescending<Pair<String, Int>> { it.second }   // 1️⃣ 빈도수 기준 내림차순
        .thenByDescending { it.first.length }                         // 2️⃣ 단어 길이 기준 내림차순
        .thenBy { it.first }                                          // 3️⃣ 알파벳 사전 순 (오름차순)
    )
    .toMap(LinkedHashMap())                                           // 순서 유지
    .forEach { println(it.key) }
```
### 작동과정
1. `dictMap.toList()`
    - `Map<String, Int>` -> `List<Pair<String, Int>>`로 변환
    - 각 요소는 `(key, value)` 형태의 `Pair`로 저장됨
2. `compareByDescending<Pair<String, Int>>`
    - `Pair`의 두 번째 요소(`value`)를 기준으로 내림차순 정렬
3. `thenByDescending { it.first.length }`
    - `Pair`의 첫 번째 요소(`key`)의 길이로 추가 정렬
4. `thenBy {it.first}`
    - 사전 순으로 최종 정렬
5. `toMap(LinkedHashMap())`
    - 순서가 유지되는 `LinkedHashMap`으로 변환하여 출력 유지