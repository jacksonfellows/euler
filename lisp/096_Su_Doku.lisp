(defun char-digit (c)
  (- (char-code c) (char-code #\0)))

(defun read-board (f)
  (let ((board (make-array '(9 9))))
    (dotimes (row 9)
      (loop for c across (read-line f)
	    for col from 0 to 8
	    do (setf (aref board row col) (char-digit c))))
    board))

(defun read-boards (filename)
  (let ((boards))
    (with-open-file (f filename)
      (loop for line = (read-line f nil)
	    while line do
	      (push (read-board f) boards)))
    (nreverse boards)))

(defparameter *boards* (read-boards "../p096_sudoku.txt"))

(defmacro collecting (&body forms)
  (let ((list (gensym)))
    `(let ((,list))
       (flet ((collect (x) (push x ,list)))
	 ,@forms)
       (nreverse ,list))))

(defun row (board row)
  (collecting (dotimes (col 9) (collect (aref board row col)))))

(defun col (board col)
  (collecting (dotimes (row 9) (collect (aref board row col)))))

(defun box (board row col)
  (let ((box-row (floor row 3)) (box-col (floor col 3)))
    (values
     (collecting
       (dotimes (i 3)
	 (dotimes (j 3)
	   (collect (aref board (+ i (* 3 box-row)) (+ j (* 3 box-col)))))))
     (list box-row box-col))))

(defparameter *nums* (loop for n from 1 to 9 collecting n))

(defun options (board)
  (let ((options (make-array '(9 9))))
    (dotimes (row 9)
      (dotimes (col 9)
	(setf (aref options row col)
	      (set-difference
	       *nums*
	       (remove
		(aref board row col)
		(reduce #'union (list (row board row) (col board col) (box board row col))))))))
    options))

(defun singlep (list)
  (and (car list) (null (cdr list))))

(defun copy-array (array)
  (let ((new-array (make-array (array-dimensions array))))
    (dotimes (i (array-total-size array))
      (setf (row-major-aref new-array i)
	    (row-major-aref array i)))
    new-array))

;; (defun array= (a b)
;;   (and (equal (array-dimensions a) (array-dimensions b))
;;        (not (dotimes (i (array-total-size a))
;; 	      (when (/= (row-major-aref a i) (row-major-aref b i))
;; 		(return t))))))

(defun duplicatesp (list)
  (some #'identity (maplist (lambda (list) (find (car list) (cdr list))) list)))

(defun is-valid (board)
  (notany #'duplicatesp
	  (mapcar (lambda (list) (remove 0 list))
		  (append (loop for row from 0 to 8 collecting (row board row))
			  (loop for col from 0 to 8 collecting (col board col))
			  (loop for r from 0 to 2 for c from 0 to 2
				collecting (box board (* 3 r) (* 3 c)))))))

(defun solve-simple (board)
  (let ((options (options board)))
    (dotimes (row 9)
      (dotimes (col 9)
	(let ((opts (aref options row col)))
	  (when (and (zerop (aref board row col)) (singlep opts))
	    (setf (aref board row col) (car opts)))))))
  board)

(defun solve (board)
  (solve-simple board)
  (when (is-valid board)
    (let ((options (options board))
	  (i (dotimes (i (array-total-size board))
	       (when (zerop (row-major-aref board i))
		 (return i)))))
      (if i
	  (let ((opts (row-major-aref options i)))
	    (dolist (opt opts)
	      (let ((new-board (copy-array board)))
		(setf (row-major-aref new-board i) opt)
		(setf new-board (solve new-board))
		(when new-board
		  (return new-board)))))
	  board))))

(defun p96 ()
    (let ((total 0))
      (dolist (board *boards*)
	(let ((solved (solve (copy-array board))))
	  (print solved)
	  (print (is-valid solved))
	  (incf total (reduce (lambda (a b) (+ (* 10 a) b))
			      (loop for col from 0 to 2 collecting (aref solved 0 col))))))
      total))
