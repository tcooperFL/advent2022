(ns day6)

(def input-data "/Users/tom/Dev/python/advent2022/data/day6.txt")

(defn solve [s n]
   (+ n (count (take-while #(< (count %) n)
                           (map set (partition n 1 (seq s)))))))

(comment
  ;; Part 1
  (solve (slurp input-data) 4)

  ;; Part 2
  (solve (slurp input-data) 14))
