;;;; euler.asd

(asdf:defsystem #:euler
  :description "Describe euler here"
  :author "Your Name <your.name@example.com>"
  :license  "Specify license here"
  :version "0.0.1"
  :serial t
  :depends-on (#:iterate #:alexandria)
  :components ((:file "package")
               (:file "utils")))
