(in-package :euler)

(defun cont-frac (terms)
  (reduce (lambda (a b) (+ a (/ b))) terms :from-end t))

(defun e-terms (n)
  (labels ((rec (k)
	     (when (< (* (1- k) 3) (1- n))
	       (cons 1 (cons (* 2 k) (cons 1 (rec (1+ k))))))))
    (subseq (cons 2 (rec 1)) 0 n)))

(defun digital-sum (n)
  (apply #'+ (num-to-digits n)))

(defun e-cont-frac (n)
  (cont-frac (e-terms n)))

(defun p65 ()
  (digital-sum (numerator (e-cont-frac 100))))
