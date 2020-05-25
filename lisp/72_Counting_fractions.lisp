(in-package #:euler)

(defun farey-n-terms (n)
  (iterate (for i from 1 to n)
    (summing (euler-phi i))))

(defun p72 ()
  (farey-n-terms 1000000))
