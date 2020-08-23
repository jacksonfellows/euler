(in-package #:euler)

(defun p69 ()
  (iterate (for n from 2 to 1000000)
    (finding n maximizing (/ n (euler-phi n)))))
