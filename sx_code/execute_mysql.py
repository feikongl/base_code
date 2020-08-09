# -*- coding: utf-8 -*-
import attr

from sx_code.exception import MySqlError


@attr.s(frozen=False, cmp=False, hash=False, repr=True)
class ExecuteMysql(object):
    db = attr.ib()

    def select_attr_fetchone(self, cls_obj, attr_name, **kwargs):
        """
        获取模型类的单个属性
        :param cls_obj: 模型类
        :param attr_name: 要获取的模型类的属性
        :param kwargs: 查询条件
        :return:
        """
        filters = list()
        try:
            for key, value in kwargs.items():
                if not hasattr(cls_obj, key):
                    raise MySqlError(f"'{cls_obj.__name__}' object has not attribution'{key}'")
                filters.append(getattr(cls_obj, key, None) == kwargs[key])
            attr = self.db.session.query(getattr(cls_obj, attr_name, None)).filter(*filters).first()
            self.db.session.close()
            return attr[0] if attr is not None else None
        except Exception as e:
            raise MySqlError(e)

    def select_attr_fetchall(self, cls_obj, attr_name, **kwargs):
        """
        获取模型类的单个属性
        :param cls_obj: 模型类
        :param attr_name: 要获取的模型类的属性
        :param kwargs: 查询条件
        :return:
        """
        filters = list()
        try:
            for key, value in kwargs.items():
                if not hasattr(cls_obj, key):
                    raise MySqlError(f"'{cls_obj.__name__}' object has not attribution'{key}'")
                filters.append(getattr(cls_obj, key, None) == kwargs[key])
            attr_list = self.db.session.query(getattr(cls_obj, attr_name, None)).filter(*filters).all()
            self.db.session.close()
            return (attr[0] for attr in attr_list)
        except Exception as e:
            raise MySqlError(e)

    def select_attrs_fetchone(self, cls_obj, attrs_name_lst, **kwargs):
        """
        获取模型类的多个属性
        :param cls_obj: 模型类
        :param attrs_name_lst: 要获取的模型类的属性列表
        :param kwargs: 查询条件
        :return:
        """
        queries = list()
        filters = list()
        try:
            for attr_name in attrs_name_lst:
                if not hasattr(cls_obj, attr_name):
                    raise MySqlError(f"'{cls_obj.__name__}' object has not attribution '{attr_name}'")
                queries.append(getattr(cls_obj, attr_name, None))
            for key, value in kwargs.items():
                if not hasattr(cls_obj, key):
                    raise MySqlError(f"'{cls_obj.__name__}' object has not attribution'{key}'")
                filters.append(getattr(cls_obj, key, None) == kwargs[key])
            attrs = self.db.session.query(*queries).filter(*filters).first()
            self.db.session.close()
            return attrs
        except Exception as e:
            raise MySqlError(e)

    def select_attrs_fetchall(self, cls_obj, attrs_name_lst, **kwargs):
        """
        获取模型类的多个属性
        :param cls_obj: 模型类
        :param attrs_name_lst: 要获取的模型类的属性列表
        :param kwargs: 查询条件
        :return:
        """
        queries = list()
        filters = list()
        try:
            for attr_name in attrs_name_lst:
                if not hasattr(cls_obj, attr_name):
                    raise MySqlError(f"'{cls_obj.__name__}' object has not attribution '{attr_name}'")
                queries.append(getattr(cls_obj, attr_name, None))
            for key, value in kwargs.items():
                if not hasattr(cls_obj, key):
                    raise MySqlError(f"'{cls_obj.__name__}' object has not attribution'{key}'")
                filters.append(getattr(cls_obj, key, None) == kwargs[key])
            attrs = self.db.session.query(*queries).filter(*filters).all()
            return attrs
        except Exception as e:
            raise MySqlError(e)

    def update_cls_attrs(self, cls_obj, attrs_name_lst, attrs_value_lst):
        """
        更新模型类的多个属性
        :param cls_obj: 模型类对象
        :param attrs_name_lst: 属性列表
        :param attrs_value_lst: 属性值列表
        :return:
        """
        try:
            for i in range(len(attrs_name_lst)):
                setattr(cls_obj, attrs_name_lst[i], attrs_value_lst[i])
            self.db.session.commit()
        except Exception as e:
            raise MySqlError(e)

    def create_new_report(self, cls_obj, **kwargs):
        """
        生成模型类对象
        :param cls_obj:
        :param kwargs:
        :return:
        """
        new_cls_report = cls_obj()
        for attr_name, attr_value in kwargs.items():
            if not hasattr(cls_obj, attr_name):
                raise AttributeError("'{}' object has not attribute '{}'".format(cls_obj.__name__, attr_name))
            setattr(new_cls_report, attr_name, attr_value)
        return new_cls_report

    def save_cls_report(self, new_report_ins):
        """
        新增记录
        :param new_report_ins:
        :return:
        """
        try:
            self.db.session.add(new_report_ins)
            self.db.session.commit()
            new_ins_id = new_report_ins.id
            return new_ins_id
        except Exception as e:
            self.db.session.rollback()
            raise MySqlError(f"execute mysql error.")

    def save_cls_reports(self, new_report_ins_list):
        """
        新增多个记录
        :param new_report_ins_list:
        :return:
        """
        try:
            for new_report_ins in new_report_ins_list:
                self.db.session.add(new_report_ins)
            self.db.session.commit()
        except Exception as e:
            self.db.session.rollback()
            raise MySqlError(f"execute mysql error.")

    def delete_cls_report(self, report_ins):
        """
        删除记录
        :param report_ins:
        :return:
        """
        try:
            self.db.session.delete(report_ins)
            self.db.session.commit()
        except Exception as e:
            self.db.session.rollback()
            raise MySqlError(f"execute mysql error.")

    def del_and_create_reports(self, del_ins_list, create_ins_lst):
        """
        删除记录 和 新增记录
        :param del_ins_list:
        :param create_ins_lst:
        :return:
        """
        try:
            for ins in del_ins_list:
                self.db.session.delete(ins)
            for ins in create_ins_lst:
                self.db.session.add(ins)
            self.db.session.commit()
        except Exception as e:
            self.db.session.rollback()
            raise MySqlError(f"execute mysql error.")

    def select_cls_fetchall(self, cls_obj, **kwargs):
        """
        查询模型对象
        :param cls_obj:
        :param kwargs:
        :return:
        """
        filters = list()
        try:
            for key, value in kwargs.items():
                if not hasattr(cls_obj, key):
                    raise MySqlError(f"'{cls_obj.__name__}' object has not attribution'{key}'")
                filters.append(getattr(cls_obj, key, None) == kwargs[key])
            cls_list = self.db.session.query(cls_obj).filter(*filters).all()
            return cls_list
        except Exception as e:
            raise MySqlError(e)

    def select_cls_fetchone(self, cls_obj, **kwargs):
        """
        查询模型对象
        :param cls_obj: 模型类
        :param kwargs: 查询条件
        :return:
        """
        filters = list()
        try:
            for key, value in kwargs.items():
                if not hasattr(cls_obj, key):
                    raise MySqlError(f"'{cls_obj.__name__}' object has not attribution'{key}'")
                filters.append(getattr(cls_obj, key, None) == kwargs[key])
            cls = self.db.session.query(cls_obj).filter(*filters).first()
            return cls
        except Exception as e:
            raise MySqlError(e)
