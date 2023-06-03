from build.ab2 import DefaultVars
from build.c import clibrary, cxxprogram

clibrary(
    name="luau",
    srcs=[
        "./Analysis/src/Anyification.cpp",
        "./Analysis/src/ApplyTypeFunction.cpp",
        "./Analysis/src/AstJsonEncoder.cpp",
        "./Analysis/src/AstQuery.cpp",
        "./Analysis/src/Autocomplete.cpp",
        "./Analysis/src/BuiltinDefinitions.cpp",
        "./Analysis/src/Clone.cpp",
        "./Analysis/src/Config.cpp",
        "./Analysis/src/Constraint.cpp",
        "./Analysis/src/ConstraintGraphBuilder.cpp",
        "./Analysis/src/ConstraintSolver.cpp",
        "./Analysis/src/DataFlowGraph.cpp",
        "./Analysis/src/DcrLogger.cpp",
        "./Analysis/src/Def.cpp",
        "./Analysis/src/EmbeddedBuiltinDefinitions.cpp",
        "./Analysis/src/Error.cpp",
        "./Analysis/src/Frontend.cpp",
        "./Analysis/src/Instantiation.cpp",
        "./Analysis/src/IostreamHelpers.cpp",
        "./Analysis/src/JsonEmitter.cpp",
        "./Analysis/src/LValue.cpp",
        "./Analysis/src/Linter.cpp",
        "./Analysis/src/Module.cpp",
        "./Analysis/src/Normalize.cpp",
        "./Analysis/src/Quantify.cpp",
        "./Analysis/src/Refinement.cpp",
        "./Analysis/src/RequireTracer.cpp",
        "./Analysis/src/Scope.cpp",
        "./Analysis/src/Substitution.cpp",
        "./Analysis/src/Symbol.cpp",
        "./Analysis/src/ToDot.cpp",
        "./Analysis/src/ToString.cpp",
        "./Analysis/src/TopoSortStatements.cpp",
        "./Analysis/src/Transpiler.cpp",
        "./Analysis/src/TxnLog.cpp",
        "./Analysis/src/Type.cpp",
        "./Analysis/src/TypeArena.cpp",
        "./Analysis/src/TypeAttach.cpp",
        "./Analysis/src/TypeChecker2.cpp",
        "./Analysis/src/TypeInfer.cpp",
        "./Analysis/src/TypePack.cpp",
        "./Analysis/src/TypeReduction.cpp",
        "./Analysis/src/TypeUtils.cpp",
        "./Analysis/src/TypedAllocator.cpp",
        "./Analysis/src/Unifiable.cpp",
        "./Analysis/src/Unifier.cpp",
        "./Ast/src/Ast.cpp",
        "./Ast/src/Confusables.cpp",
        "./Ast/src/Lexer.cpp",
        "./Ast/src/Location.cpp",
        "./Ast/src/Parser.cpp",
        "./Ast/src/StringUtils.cpp",
        "./Ast/src/TimeTrace.cpp",
        "./CodeGen/src/AssemblyBuilderA64.cpp",
        "./CodeGen/src/AssemblyBuilderX64.cpp",
        "./CodeGen/src/CodeAllocator.cpp",
        "./CodeGen/src/CodeBlockUnwind.cpp",
        "./CodeGen/src/CodeGen.cpp",
        "./CodeGen/src/CodeGenUtils.cpp",
        "./CodeGen/src/CodeGenX64.cpp",
        "./CodeGen/src/EmitBuiltinsX64.cpp",
        "./CodeGen/src/EmitCommonX64.cpp",
        "./CodeGen/src/EmitInstructionX64.cpp",
        "./CodeGen/src/Fallbacks.cpp",
        "./CodeGen/src/IrAnalysis.cpp",
        "./CodeGen/src/IrBuilder.cpp",
        "./CodeGen/src/IrDump.cpp",
        "./CodeGen/src/IrLoweringX64.cpp",
        "./CodeGen/src/IrRegAllocX64.cpp",
        "./CodeGen/src/IrTranslateBuiltins.cpp",
        "./CodeGen/src/IrTranslation.cpp",
        "./CodeGen/src/IrUtils.cpp",
        "./CodeGen/src/NativeState.cpp",
        "./CodeGen/src/OptimizeConstProp.cpp",
        "./CodeGen/src/OptimizeFinalX64.cpp",
        "./CodeGen/src/UnwindBuilderDwarf2.cpp",
        "./CodeGen/src/UnwindBuilderWin.cpp",
        "./Compiler/src/BuiltinFolding.cpp",
        "./Compiler/src/Builtins.cpp",
        "./Compiler/src/BytecodeBuilder.cpp",
        "./Compiler/src/Compiler.cpp",
        "./Compiler/src/ConstantFolding.cpp",
        "./Compiler/src/CostModel.cpp",
        "./Compiler/src/TableShape.cpp",
        "./Compiler/src/ValueTracking.cpp",
        "./Compiler/src/lcode.cpp",
        "./VM/src/lapi.cpp",
        "./VM/src/laux.cpp",
        "./VM/src/lbaselib.cpp",
        "./VM/src/lbitlib.cpp",
        "./VM/src/lbuiltins.cpp",
        "./VM/src/lcorolib.cpp",
        "./VM/src/ldblib.cpp",
        "./VM/src/ldebug.cpp",
        "./VM/src/ldo.cpp",
        "./VM/src/lfunc.cpp",
        "./VM/src/lgc.cpp",
        "./VM/src/lgcdebug.cpp",
        "./VM/src/linit.cpp",
        "./VM/src/lmathlib.cpp",
        "./VM/src/lmem.cpp",
        "./VM/src/lnumprint.cpp",
        "./VM/src/lobject.cpp",
        "./VM/src/loslib.cpp",
        "./VM/src/lperf.cpp",
        "./VM/src/lstate.cpp",
        "./VM/src/lstring.cpp",
        "./VM/src/lstrlib.cpp",
        "./VM/src/ltable.cpp",
        "./VM/src/ltablib.cpp",
        "./VM/src/ltm.cpp",
        "./VM/src/ludata.cpp",
        "./VM/src/lutf8lib.cpp",
        "./VM/src/lvmexecute.cpp",
        "./VM/src/lvmload.cpp",
        "./VM/src/lvmutils.cpp",
    ],
    vars=DefaultVars
    + {
        "+includes": [
            "-I./third_party/luau/Analysis/include",
            "-I./third_party/luau/Ast/include",
            "-I./third_party/luau/CodeGen/include",
            "-I./third_party/luau/Common/include",
            "-I./third_party/luau/Compiler/include",
            "-I./third_party/luau/VM/include",
            "-I./third_party/luau/VM/src",
        ]
    },
    exportvars={
        "+includes": [
            "-I./third_party/luau/Analysis/include",
            "-I./third_party/luau/Ast/include",
            "-I./third_party/luau/CodeGen/include",
            "-I./third_party/luau/Common/include",
            "-I./third_party/luau/Compiler/include",
            "-I./third_party/luau/VM/include",
        ]
    },
)

cxxprogram(
    name="analyse",
    srcs=[
        "./CLI/Analyze.cpp",
        "./CLI/FileUtils.cpp",
        "./CLI/Flags.cpp",
    ],
    deps=["+luau"],
    vars=DefaultVars
    + {
        "+includes": [
            "-I./src/c/luau/Analysis/include",
            "-I./src/c/luau/Ast/include",
            "-I./src/c/luau/CodeGen/include",
            "-I./src/c/luau/Common/include",
            "-I./src/c/luau/Compiler/include",
            "-I./src/c/luau/VM/include",
            "-I./src/c/luau/VM/src",
        ]
    },
)