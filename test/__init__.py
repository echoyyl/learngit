import jpype


jpype.startJVM(jpype.getDefaultJVMPath())
jpype.java.lang.System.out.println("I love Yali!")
jpype.shutdownJVM()