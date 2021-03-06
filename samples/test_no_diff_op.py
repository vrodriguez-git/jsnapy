tests_include:
  - test_1_element_no_id_pass_1_value
  - test_1_element_with_id_same_node_name_pass_1_value
  - test_1_element_with_id_diff_node_name_pass_1_value
  - test_1_element_with_2_id_diff_node_name_pass_1_value
  - test_1_element_with_id_diff_node_name_fail_1_value
  - test_1_element_with_id_diff_node_name_diff_id_fail_2_value
  - test_1_element_with_id_diff_node_name_diff_id_pass_1_fail_1_value
  - test_2_element_with_id_diff_node_name_pass_2_value

test_1_element_no_id_pass_1_value:
 - command: show summary
 - item:
    xpath: //summary/count[@style='state']
    id: .
    tests:
        - no-diff: active
          err: ' Failed!!change from {{pre["active"]}} to {{post["active"]}}'
          info: 'Details is pre <{{id_0}}> : {{pre["active"]}} and post <{{id_0}}> : {{post["active"]}}'

test_1_element_with_id_same_node_name_pass_1_value:
 - command: show summary
 - iterate:
    xpath: //summary/count[@style='state']
    id: active
    tests:
        - no-diff: active
#        - no-diff: 
          err: ' Failed!! change from {{pre["active"]}} to {{post["active"]}}'
          info: 'Details is pre <{{id_0}}> : {{pre["active"]}} and post <{{id_0}}> : {{post["active"]}}'

test_1_element_with_id_diff_node_name_pass_1_value:
 - command: show summary
 - iterate:
    xpath: //summary/count[@style='state']
    id: key
    tests:
        - no-diff: active
          err: ' Failed!! change from {{pre["active"]}} to {{post["active"]}}'
          info: 'Details is 1st <{{id_0}}> : {{pre["active"]}} and 2nd <{{id_0}}> : {{post["active"]}}'

test_1_element_with_2_id_diff_node_name_pass_1_value:
 - command: show summary
 - iterate:
    xpath: //summary/count[@style='state']
    id: active, key
    tests:
        - no-diff: active
          err: ' Failed!! change from {{pre["active"]}} to {{post["active"]}}'
          info: 'Details is 1st <{{id_0}}>,<{{id_1}}> : {{pre["active"]}} and 2nd <{{id_0}}>,<{{id_1}}> : {{post["active"]}}'

test_1_element_with_id_diff_node_name_fail_1_value:
 - command: show summary
 - iterate:
    xpath: //summary/count[@style='state']
    id: active
    tests:
        - no-diff: style
          err: 'Failed!! change from {{pre["style"]}} to {{post["style"]}}'
          info: 'Details is pre <{{id_0}}> : {{pre["style"]}} and pre <{{id_0}}> : {{post["style"]}}'

test_1_element_with_id_diff_node_name_diff_id_fail_2_value:
 - command: show summary
 - iterate:
    xpath: //summary/count[@style='state']
    id: style
    tests:
        - no-diff: total 
          err: 'Failed!! change from pre <{{id_0}}> : {{pre["total"]}} to post <{{id_0}}> : {{post["total"]}}'
          info: 'Details is pre <{{id_0}}> : {{pre["total"]}} and post <{{id_0}}> : {{post["total"]}}'

test_1_element_with_id_diff_node_name_diff_id_pass_1_fail_1_value:
 - command: show summary
 - iterate:
    xpath: //summary/system
    id: status
    tests:
        - no-diff: count 
          err: 'Failed!! change from pre <{{id_0}}> : {{pre["count"]}} to post <{{id_0}}> : {{post["count"]}}'
          info: 'Details is pre <{{id_0}}> : {{pre["count"]}} and post <{{id_0}}> : {{post["count"]}}'

test_2_element_with_id_diff_node_name_pass_2_value:
 - command: show summary
 - iterate:
    xpath: //summary/count[@style='value']
    id: id
    tests:
        - no-diff: session
          err: ' Failed!! Total session change from {{pre["session"]}} to {{post["session"]}}'
          info: 'Details is pre <{{id_0}}> : {{pre["session"]}} and post <{{id_0}}> : {{post["session"]}}'

