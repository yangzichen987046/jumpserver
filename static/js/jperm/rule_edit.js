/**
 * Created by A on 2016/3/3.
 */

                                $(document).ready(function(){
                               $("select").mouseover(function(){
                                     $("select").attr("disabled","disabled");
                                    });
                                     $("body").mouseout(function(){
                                    $("select").removeAttr("disabled");
                                    });
                                    });
