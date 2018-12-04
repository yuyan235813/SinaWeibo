#!/usr/bin/python
# -*- coding: utf-8 -*-
from SinaWeibo import Weibo
from SinaWeibo import Push

if __name__ == '__main__':
    wb= Weibo("yuyan235813","yy12y090812y")
    # wb.comment('https://weibo.com/6868475304/H5HTi6523?from=page_1005056868475304_profile&wvr=6&mod=weibotime&type=comment#_rnd1543931259207',
    #            'https://weibo.com/6868475304/H5HTi6523?from=page_1005056868475304_profile&wvr=6&mod=weibotime&type=comment',
    #            'test')
    push = Push(wb)
    push.like_publish("https://weibo.com/6868475304/H5HTi6523?from=page_1005056868475304_profile&wvr=6&mod=weibotime&type=comment#_rnd1543931259207")
    # wb.postMessage("0.2测试1:文本")
    # time.sleep(1)
    # wb.postImage("0.2测试2:一张图片","/Downloads/4.png")
    # time.sleep(1)
    # wb.postImage("0.2测试3:多张图片","/Downloads/4.png","/Downloads/5.jpg")
    #
    # # 我的关注
    # pageNum = 1
    # followList, hasNext = wb.getFollowList(pageNum)
    # print(followList)
    # while hasNext == True:
    #     pageNum = pageNum + 1
    #     followList, hasNext = wb.getFollowList(pageNum)
    #     print(followList)
    #
    # # 我的粉丝
    # pageNum = 1
    # fansList , hasNext = wb.getFansList(pageNum)
    # print(fansList)
    # while hasNext == True:
    #     pageNum = pageNum + 1
    #     fansList, hasNext = wb.getFansList(pageNum)
    #     print(fansList)
    #
    # # 我的微博
    # blogList = wb.getMyBlogList(1)
    # for blog in blogList:
    #     print(blog)


