#ifndef STUDENT_H
#define STUDENT_H

#include <QObject>

class Student : public QObject
{
    Q_OBJECT
public:
    explicit Student(QObject *parent = nullptr);
    //slots 返回值为void ，需要声明实现，可以有参数，重载
  //  void treat();

    void treat(QString foodName);
signals:



};

#endif // STUDENT_H
