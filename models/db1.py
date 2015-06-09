# -*- coding: utf-8 -*-
db.define_table('blog_post',
                Field('Title',requires=IS_NOT_EMPTY()),
                Field( 'Description','text',requires=IS_NOT_EMPTY()),
                Field('Tags',requires=IS_NOT_EMPTY()),
                Field('Author',requires=IS_NOT_EMPTY()),
                Field('time_stamp','datetime'))
