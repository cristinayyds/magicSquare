/* 实例窗体源文件 */
#include "mainwindow.h"
#include "ui_mainwindow.h"
#include <QLabel>

MainWindow::MainWindow(QWidget *parent):
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    this->setWindowTitle("移动无边框窗体");
    this->setWindowFlag(Qt::WindowMaximizeButtonHint);

    btClose = new QPushButton(this);
    btClose->setText("关闭");
    connect(btClose,SIGNAL(clicked()),this,SLOT(close()));
    this->setWindowIcon(QIcon(":/new/prefix1/img1"));
    button = new QPushButton(this);
    button->setGeometry(QRect(50,50,100,25));
    button->setText("按钮");
    connect(button,SIGNAL(clicked()),this,SLOT(showMainwindow2()));

/*
    // 创建一个QLable控件
    QLabel *label = new QLabel(this);
    // QLabel控件的文字内容
    label->setText("rubbish nuaa's library which only has few useful charging ports.");
    // 显示位置
    label->setGeometry(QRect(200,200,500,100));
*/
}

MainWindow::~MainWindow()
{
    delete ui;
}
/*
void MainWindow::mousePressEvent(QMouseEvent *e)
{
    last = e->globalPos();
}

void MainWindow::mouseMoveEvent(QMouseEvent *e)
{
    int dx = e->globalX()-last.x();
    int dy = e->globalY()-last.y();
    last = e->globalPos();
    move(x()+dx,y()+dy);
}
void MainWindow::mouseReleaseEvent(QMouseEvent *e)
{
    int dx = e->globalX()-last.x();
    int dy = e->globalY()-last.y();
    move(x()+dx,y()+dy);
}
*/
void MainWindow::showMainwindow2()
{

    w2.show();
}
