(in-package #:euler)

(defun fracs-in-range (low-n low-d high-n high-d max-d)
  (let ((mid-n (+ low-n high-n))
	(mid-d (+ low-d high-d)))
    (if (> mid-d max-d)
	0
	(+ 1
	   (fracs-in-range low-n low-d mid-n mid-d max-d)
	   (fracs-in-range mid-n mid-d high-n high-d max-d)))))

(defun p73 ()
  (fracs-in-range 1 3 1 2 12000))
