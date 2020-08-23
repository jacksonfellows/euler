#lang racket
(define pwr 5)
(define (to-pwr n) (expt n pwr))
(define max-pwr (expt 10 (+ pwr 1)))
(define (get-digits n) (let-values ([(quot rem) (quotient/remainder n 10)])
                          (if (zero? quot) (list rem)
                              (cons rem (get-digits quot)))))
(define (pwr-digit-sum n) (apply + (map to-pwr (get-digits n))))
(define writeable (filter (lambda (n) (= n (pwr-digit-sum n))) (build-list max-pwr values)))
(- (apply + writeable) 1) ; 1 doesn't count