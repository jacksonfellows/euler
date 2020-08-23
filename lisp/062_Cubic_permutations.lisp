(in-package #:euler)

(defparameter *cube-perms* (make-hash-table))
(defparameter *first-perm* (make-hash-table))

(defun p62 ()
  (do* ((n 1 (1+ n))
	(cube 1 (expt n 3))
	(sorted 1 (sorted-digits cube)))
       ((= 5 (incf (gethash sorted *cube-perms* 0))) (values (gethash sorted *first-perm*) n cube))
    (when (not (gethash sorted *first-perm*))
      (setf (gethash sorted *first-perm*) cube))))

