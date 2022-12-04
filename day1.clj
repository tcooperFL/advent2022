(ns day1
  (:require [clojure.java.io :as io]))

(def input-data "/Users/tom/Dev/python/advent2022/data/day1.txt")

(defn total [lst]
  (reduce + (map #(Integer/parseInt %) lst)))

(defn solve [file]
  (with-open [rdr (io/reader file)]
    (doall
     (map total
          (remove #{'("")}
                  (partition-by #{""} (line-seq rdr)))))))

(comment
  ;; Part 1
  (apply max (solve input-data))

  ;; Part 2
  (apply + (take 3 (sort-by - (solve input-data))))
  :rcf)