#include <linux/kernel.h>
#include <linux/module.h>
#include <linux/init.h>
#include <linux/fs.h>
#include <asm/uaccess.h>

MODULE_LICENSE( "GPL" );
MODULE_AUTHOR( "Bakanov Roman" );
MODULE_DESCRIPTION( "Trying to create a module" );
MODULE_SUPPORTED_DEVICE( "inc" ); 

#define SUCCESS 0
#define DEVICE_NAME "inc" 

static int device_open( struct inode *, struct file * );
static int device_release( struct inode *, struct file * );
static ssize_t device_read( struct file *, char *, size_t, loff_t * );
static ssize_t device_write( struct file *, const char *, size_t, loff_t * );

static int sequence = 0;
static int major_number;
static int is_device_open = 0;

static struct file_operations fops =
 {
  .read = device_read,
  .write = device_write,
  .open = device_open,
  .release = device_release
 };

static int __init inc_init( void )
{
 printk( KERN_ALERT "Incremental driver loaded!\n" );
 major_number = register_chrdev( 0, DEVICE_NAME, &fops );
 if ( major_number < 0 )
 {
  printk( "Registering the character device failed with %d\n", major_number );
  return major_number;
 }
 printk( "Incremental module is loaded!\n" );
 printk( "Please, create a dev file with 'mknod /dev/inc c %d 0'.\n", major_number );
 return SUCCESS;
}

static void __exit inc_exit( void )
{
 unregister_chrdev( major_number, DEVICE_NAME );
 printk( KERN_ALERT "Incremental module is unloaded!\n" );
}

module_init( inc_init );
module_exit( inc_exit );

static int device_open( struct inode *inode, struct file *file )
{
 if ( is_device_open )
  return -EBUSY;
 is_device_open++;
 return SUCCESS;
}

static int device_release( struct inode *inode, struct file *file )
{
 is_device_open--;
 return SUCCESS;
}

static ssize_t device_write( struct file *filp,
       const char *buff,
       size_t len,
       loff_t * off )
{
 printk( "Sorry, this operation isn't supported.\n" );
 return -EINVAL;
}

static ssize_t device_read( struct file *filp,
       char *buffer,
       size_t length,
       loff_t * offset )
{
 sequence++;
 copy_to_user(buffer, &sequence, length);
 return sequence;
}
