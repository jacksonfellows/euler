(in-package #:euler)

(defmacro defun-memo (name lambda-list &key (test ''equal) (memo-form `(list ,@lambda-list)) body)
  (with-gensyms (table value exists)
    `(let ((,table (make-hash-table :test ,test)))
       (defun ,name ,lambda-list
	 (multiple-value-bind (,value ,exists) (gethash ,memo-form ,table)
	   (if ,exists
	       ,value
	       (setf (gethash ,memo-form ,table) (progn ,body))))))))

(defun-memo prime-factors (n)
  :test 'eql
  :memo-form n
  :body
  (iterate (for x from 2 to (isqrt n))
    (when (zerop (mod n x))
      (return (cons x (prime-factors (/ n x)))))
    (finally (return (list n)))))

(defun unique-prime-factors (n)
  (remove-duplicates (prime-factors n) :test #'=))

(defun euler-phi (n)
  (* n (iterate (for factor in (unique-prime-factors n))
	 (multiplying (- 1 (/ factor))))))

;; All of these functions work on "backwards" lists
(defun num-to-digits (num)
  (if (> 10 num)
      (list num)
      (multiple-value-bind (q r) (floor num 10)
	(cons r (num-to-digits q)))))

(defun digits-to-num (digits)
  (if digits
      (+ (car digits) (* 10 (digits-to-num (cdr digits))))
      0))

(defun sorted-digits (num)
  (digits-to-num (sort (num-to-digits num) #'<)))
