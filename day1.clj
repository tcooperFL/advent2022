(ns day1
  (:require [clojure.java.io :as io]))

(def input-data "/Users/tom/Dev/python/advent2022/data/day1.txt")

(defn total [lst]
  (reduce + (map #(Integer/parseInt %) lst)))

(defn part1 [file]
  (with-open [rdr (io/reader file)]
    (apply max
           (map total
                (remove #{'("")}
                        (partition-by #{""} (line-seq rdr)))))))

(comment
  (part1 input-data) 
  :rcf)