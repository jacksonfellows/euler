(declaim (optimize (speed 3) (safety 0)))

;; (defun longest-non-increasing-suffix-index (seq)
;;   (do ((i (1- (length seq)) (1- i)))
;;       ((or (= i 0) (> (elt seq i) (elt seq (1- i)))) i)))

;; (defun find-rightmost-succ (seq i)
;;   (do ((j (1- (length seq)) (1- j)))
;;       ((and (>= j i) (> (elt seq j) (elt seq (1- i)))) j)))

;; (defun reverse-subseq (seq &optional (from 0) (to (length seq)))
;;   (do ((i from (1+ i))
;;        (j (1- to) (1- j)))
;;       ((>= i j) seq)
;;     (rotatef (aref seq i) (aref seq j))))

;; (defun next-perm (seq)
;;   (let ((i (longest-non-increasing-suffix-index seq)))
;;     (when (< 0 i)
;;       (let ((j (find-rightmost-succ seq i)))
;; 	(rotatef (aref seq (1- i)) (aref seq j))
;; 	(reverse-subseq seq i)))))

;; (defun prime-factors (n)
;;   (loop for x from 2 to (isqrt n)
;; 	when (zerop (mod n x))
;; 	  return (cons x (prime-factors (/ n x)))
;; 	finally (return (list n))))

;; (defun triplets? (sorted-list)
;;   (if (not sorted-list)
;;       t
;;       (ignore-errors
;;        (destructuring-bind (a b c . rest) sorted-list
;; 	 (and (= a b c)
;; 	      (triplets? rest))))))

;; (defun digital-sum (n)
;;   (if (zerop n)
;;       0
;;       (multiple-value-bind (q r) (floor n 10)
;; 	(+ r (digital-sum q)))))

;; (defun digital-root (n)
;;   (if (< n 10)
;;       n
;;       (digital-root (digital-sum n)))))

;; (defun cube-digital-root? (n)
;;   (let ((rt (digital-root n)))
;;     (or (= 1 rt)
;; 	(= 8 rt)
;; 	(= 9 rt))))

;; (defun cube? (n)
;;   (and (cube-digital-root? n) (triplets? (prime-factors n))))

;; (defvar *num-cubes* 10000)
;; (defvar *cubes* (make-hash-table :size *num-cubes*))

;; (defun fill-cubes ()
;;   (dotimes (n *num-cubes*)
;;     (setf (gethash (expt (1+ n) 3) *cubes*) t)))

;; (defun cube? (n) (gethash n *cubes*))

;; (defun cube-perms-count (cube)
;;   (do* ((cube-seq (num-to-digits cube) (next-perm cube-seq))
;; 	(cube-num cube (digits-to-num cube-seq))
;; 	(count 1 (if (cube? cube-num)
;; 		     (1+ count)
;; 		     count)))
;;        ((not cube-seq) count)))

;; (defun p62 ()
;;   (do* ((n 1 (1+ n))
;; 	(cube 1 (expt n 3)))
;;        ((= 5 (cube-perms-count cube)) (values n cube))
;;     (print n)))

(defun num-to-digits (num)
  (let* ((len (1+ (floor (log num 10))))
	 (digits (make-array len)))
    (do ((i (1- len) (1- i))
	 (r (rem num 10) (rem num 10))) ; TODO: combine floor and rem
	((< i 0) digits)
      (setf num (floor num 10))
      (setf (aref digits i) r))))

(defun digits-to-num (digits)
  (do ((i 0 (1+ i))
       (num 0 (+ (* (expt 10 (- (length digits) 1 i)) (elt digits i)) num)))
      ((= i (length digits)) num)))

(defun sorted-digits (num)
  (digits-to-num (sort (num-to-digits num) #'>)))

(defparameter *cube-perms* (make-hash-table))
(defparameter *first-perm* (make-hash-table))

(defun p62 ()
  (do* ((n 1 (1+ n))
	(cube 1 (expt n 3))
	(sorted 1 (sorted-digits cube)))
       ((= 5 (incf (gethash sorted *cube-perms* 0))) (values (gethash sorted *first-perm*) n cube))
    (when (not (gethash sorted *first-perm*))
      (setf (gethash sorted *first-perm*) cube))))
