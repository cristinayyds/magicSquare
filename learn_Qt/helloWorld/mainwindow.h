/* 实例头文件 */
#ifndef MAINWINDOW_H
#define MAINWINDOW_H
#include <QMouseEvent>
#include <QPushButton>
#include <QMainWindow>
#include <QLabel>
#include <mainwindow2.h>

QT_BEGIN_NAMESPACE
namespace Ui { class MainWindow; }
QT_END_NAMESPACE

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    MainWindow(QWidget *parent = nullptr);
    ~MainWindow();

private:
    Ui::MainWindow *ui;
    QPushButton *btClose;
    QPushButton *button;
    MainWindow2 w2;
   // QPoint last;
private slots:
    void showMainwindow2();
/*protected:
    void mousePressEvent(QMouseEvent *e);
    void mouseMoveEvent(QMouseEvent *e);
    void mouseReleaseEvent(QMouseEvent *e);
*/
};
#endif // MAINWINDOW_H
