(in-package #:euler)

(defun p70 ()
  (iterate (for n from 2 to 10000000)
    (let ((phi (euler-phi n)))
      (when (= (sorted-digits n) (sorted-digits phi))
	(finding n minimizing (/ n phi))))))
