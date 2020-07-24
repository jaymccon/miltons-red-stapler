# Miltons::Red::Stapler

A demo resource for the AWS CloudFormation CLI written in Python with at least 3 more pieces of flair than Brian.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Miltons::Red::Stapler",
    "Properties" : {
        "<a href="#memo" title="Memo">Memo</a>" : <i>String</i>,
        "<a href="#secondcopyofmemo" title="SecondCopyOfMemo">SecondCopyOfMemo</a>" : <i>String</i>,
    }
}
</pre>

### YAML

<pre>
Type: Miltons::Red::Stapler
Properties:
    <a href="#memo" title="Memo">Memo</a>: <i>String</i>
    <a href="#secondcopyofmemo" title="SecondCopyOfMemo">SecondCopyOfMemo</a>: <i>String</i>
</pre>

## Properties

#### Memo

The memo contents.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecondCopyOfMemo

In case you didn't get the first one.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the TPSCode.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### TPSCode

A TPS Code is automatically generated on creation and assigned as the unique identifier.

#### PrintableMemo

Printable copy including Generated c over sheet.

