from collections import defaultdict


def accountsMerge(accounts):
    """
    :type accounts: List[List[str]]
    :rtype: List[List[str]]
    """
    #每个邮箱是一个节点，如果出现在同一个账户中，就连起来。最终找出所有连通，每个分量是一组可以合并的邮箱。
    # 写题目的时候不用把union find 类全部写出来，只要实现parent[] or {} 和find()，union()就可以了

    # 1. 实现简单的union find
    parent = {} # son_email -> parent_email

    def find(email):
        if parent[email] != email: # 父email非自己，即还没有找到根
            parent[email] = find(parent[email])
        return parent[email]
    def union(email1, email2):
        email1_parent = find(email1)
        email2_parent = find(email2)
        parent[email1_parent] = email2_parent

    # 2. 初始化：每一个email是一个节点
    email_and_name = {} # email -> name
    for acc in accounts:
        name = acc[0]
        for email in acc[1:]:
            if email not in parent:
                parent[email] = email # 和union-find一样，初始化的时候，父节点就是自己
            email_and_name[email] = name # 讲这个email和他的name连起来
        # 现在把同一个账户里的所有邮箱先连起来，因为她们肯定是属于一个人的
        email_1 = acc[1]
        for email_rest in acc[2:]:
            union(email_1, email_rest)

    # 3.
    roots = defaultdict(list) # root_email -> [e1, e2, e3, e4,...]
    for email in parent:
        roots[find(email)].append(email)

    # 4. output
    res = []
    for root_email, emails_list in roots.items():
        name = email_and_name[root_email]
        emails_list = sorted(emails_list)
        res.append([name] + emails_list)
    return res

accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
print(accountsMerge(accounts))








